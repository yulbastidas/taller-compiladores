import subprocess
import paramiko


class Executor:
    def __init__(self, nodes, simulate=False):
        self.nodes = nodes
        self.simulate = simulate

    def run_local_simulation(self, node_name, script_name):
        print(f"[SIMULACION] Ejecutando {script_name} en {node_name}")
        return {
            "node": node_name,
            "script": script_name,
            "status": "success",
            "output": f"Simulación de {script_name} en {node_name}"
        }

    def run_remote_script(self, node_name, script_name):
        if node_name not in self.nodes:
            return {
                "node": node_name,
                "script": script_name,
                "status": "error",
                "output": f"Nodo {node_name} no existe en nodes.json"
            }

        if self.simulate:
            return self.run_local_simulation(node_name, script_name)

        host = self.nodes[node_name]["ip"]
        user = self.nodes[node_name]["user"]
        remote_path = f"/home/{user}/cluster/scripts/{script_name}"

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=host, username=user)

            stdin, stdout, stderr = ssh.exec_command(f"bash {remote_path}")
            output = stdout.read().decode()
            error = stderr.read().decode()

            ssh.close()

            if error.strip():
                return {
                    "node": node_name,
                    "script": script_name,
                    "status": "error",
                    "output": error
                }

            return {
                "node": node_name,
                "script": script_name,
                "status": "success",
                "output": output
            }

        except Exception as e:
            return {
                "node": node_name,
                "script": script_name,
                "status": "error",
                "output": str(e)
            }

    def update_group(self, group_name, groups):
        if group_name not in groups:
            return [{
                "group": group_name,
                "status": "error",
                "output": f"Grupo {group_name} no existe"
            }]

        results = []
        for node_name in groups[group_name]:
            results.append(self.run_remote_script(node_name, "update.sh"))
        return results

    def deploy_app(self, app_name, group_name, groups):
        if group_name not in groups:
            return [{
                "group": group_name,
                "status": "error",
                "output": f"Grupo {group_name} no existe"
            }]

        script_name = f"deploy_{app_name}.sh"
        results = []
        for node_name in groups[group_name]:
            results.append(self.run_remote_script(node_name, script_name))
        return results
        
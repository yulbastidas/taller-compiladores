nodo1.run("backup.sh")

grupoA.update()

deploy app1 to grupoA

parallel {
    nodo2.run("backup.sh")
    nodo3.run("backup.sh")
}
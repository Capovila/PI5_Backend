import express from 'express'
import * as db from './database.js'

const app = express()

app.get("/notes", async(req, res) => {
    const response = await db.getAllData()
    res.send(response)
})

app.get("/notes/:id", async(req, res) => {
    const id = req.params.id
    const response = await db.getDataById(id)
    res.send(response)
})

app.use((err, req, res, next) => {
    console.log(err.stack)
    res.status(500).send("Somehting broke")
})

app.listen(8080, () =>{
    console.log("Server running at 8080")
})
import mysql from 'mysql2'
import dotenv from 'dotenv'
dotenv.config()

const pool = mysql.createPool({
    host: process.env.HOST,
    user: process.env.LOCAL_USER,
    password: process.env.PASSWORD,
    database: process.env.DATABASE
}).promise()



export async function getAllData(){
    const response = await pool.query(`SELECT * FROM Notes`)
    return response[0]
}

export async function getDataById(id){
    const response = await pool.query(`SELECT * FROM Notes WHERE id= ?`, [id])
    return response[0]
}

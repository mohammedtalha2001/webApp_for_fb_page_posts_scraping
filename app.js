// const mysql = require('mysql2');
// const express= require('express')
// const app = express()

// // const BodyParser = require('body-parser')
// const cors = require('cors')
 
// app.use(cors())
// app.use(express.json())
// // app.use(BodyParser.urlencoded({ extended: true }))

// const con = mysql.createConnection({
//     host: 'localhost',
//     user: 'root',
//     password: '123456',
//     database: 'new_schema'
//   });
//   // app.get("/api", (req,res)=>{
//   //   const mySQL = req.query.sql
//   //   con.query(
//   //       'SELECT * FROM new_schema.comments',
//   //       function(err, results, fields) {
//   //          console.log(err);
//   //         console.log("results",results); // results contains rows returned by server
    
//   //       }
//   //     );
//   // })

// // app.listen(3022, () => {
// //     console.log('Hello MySQL Server')
// // });
 
//   con.query(
//     'SELECT * FROM new_schema.comments',
//     function(err, results, fields) {
       
//       console.log("results",results); // results contains rows returned by server

//     }
//   );
// // const mysql = require('mysql');

// // // Create a MySQL connection pool
// // const pool = mysql.createPool({
// //   host: 'localhost',
// //   user: 'root',
// //   password: '123456',
// //   database: 'new_schema'
// // });

// // // Function to execute a MySQL query
// // async function query(sql, values) {
// //   return new Promise((resolve, reject) => {
// //     pool.query(sql, values, (error, results) => {
// //       if (error) {
// //         reject(error);
// //       } else {
// //         resolve(results);
// //       }
// //     });
// //   });
// // }

// // // Example usage of the query function
// // async function example() {
// //   try {
// //     const results = await query('SELECT * FROM new_schema.comments', [1]);
// //     console.log(results);
// //   } catch (error) {
// //     console.error(error);
// //   }
// // }

// // example();


const express = require("express")
const mysql = require('mysql2');
const app = express()
const cors = require("cors")
app.use(express.json())
app.use(cors())
const con = mysql.createConnection({
      host: 'localhost',
      user: 'root',
      password: '123456',
      database: 'new_schema'
    }); 

app.get("/api",(req,res)=>{
  con.query(
            'SELECT * FROM new_schema.comments',
            function(err, results, fields) {
               console.log(err);
              console.log("results",results); // results contains rows returned by server
             res.send(results)
            }
          );
})

app.listen("3100", function () {
  console.log("Node Started..");
})
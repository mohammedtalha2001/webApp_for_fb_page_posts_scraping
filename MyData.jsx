import React, { Component, useState } from 'react';
import axios from 'axios';
import { render } from '@testing-library/react';
import './tables.css';


const MyData = () => {
    let arr = []
    const [ata, setAta] = useState([])
    let count = 0;
    const handledata = async () => {
        count++
        console.log("here");
        await axios.get("http://localhost:3100/api")
            .then((res) => {
                for (let index = 0; index < res.data.length; index++) {
                    console.log("res.data[index]", res.data[index]);
                    arr.push(res.data[index])

                }
                setAta(arr)
            }
            );

        console.log("ata.length", ata.length)
        console.log("ata", ata)

    }

    return (
        <>
            <button onClick={handledata} className="btnn btn-primary">Load Data</button>
            {/* <input type="submit" onClick={handledata} /> */}
            <table className="record-table">
                <thead >
                    <tr >
                        <th>Serial No.</th>
                        <th>Page name</th>
                        <th>Post number</th>
                        <th>Poster</th>
                        <th>Post Description</th>
                        <th>Post Comments</th>
                    </tr>
                </thead>
                <tbody>
                    {ata.length > 0 ? ata.map((val, index) => {
                        return (

                            <tr >
                                <td>{val.srno}</td>
                                <td>{val.grpid}</td>
                                <td>{val.postid}</td>
                                <td>{val.poster}</td>
                                <td>{val.description}</td>
                                <td>{val.comments}</td>
                            </tr>

                        )
                    }) : <h5 className='h5'>Load Data First</h5>
                    }
                </tbody>
            </table>
            {/* // <div>
                    //     <h1>name is{val.comments}</h1>
                    //     <h1>name is {val.description}</h1>
                    //     <h1>name is {val.grpid}</h1>
                    //     <h1>name is {val.poster}</h1>
                    // </div> */}

        </>
    )
}


export default MyData;

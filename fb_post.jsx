import React , { useState }from 'react';
import MyData from './MyData';
import axios from 'axios';
// import { fetch } from 'react-dom';
import './tables.css';

const Fb_post =()=>{

  // function Button() {
    // const handleClick = () => {
    //   axios.post('http://127.0.0.1:8000/run-python-script', {})
    //     .then(response => console.log(response.data))
    //     .catch(error => console.log(error));
    // }
  // }
  const [inputValue1, setInputValue1] = useState('');
  const [inputValue2, setInputValue2] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      let config = {
        headers: {
          "Access-Control-Allow-Origin": "*"
        }
      };
      const response = await axios.post('http://127.0.0.1:8000/send-data', {
        input1: inputValue1,
        input2: inputValue2,
      },config);
      console.log(response.data);
    } catch (error) {
      console.error("ERROR: ",error);
    }
  };

  return (
    <div>
      <div className='top-div'>
        <h3 className='heading'>
          Facebook Posts scraping
        </h3>
      </div>
    <div className="container">

    <form onSubmit={handleSubmit}>
      <div className="form-group">
      <label>
        Enter page name : &nbsp;
        <input type="text" className="form-control" placeholder='page name here' size="37" value={inputValue1} onChange={e => setInputValue1(e.target.value)} />
      </label>
      </div>
      
      <div className="form-group">
      <label>
        Number of posts you want to scrape : &nbsp;
        <input type="number" className="form-control" placeholder='write in numbers(int)' size="10" value={inputValue2} onChange={e => setInputValue2(e.target.value)} />
      </label>
      </div>
      
      <button type="submit" className="btn btn-primary">Submit</button>
    </form>
    </div>
    <br />
    <MyData/>
    </div>
  );

}
    

export default Fb_post;
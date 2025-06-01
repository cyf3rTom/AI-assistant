import { useState } from 'react'
import viteLogo from '../assets/chatbot.png'
import '../App.css'
import axios from "axios"
// import email from './EmailCollector'



function App() {
  const [question, setQuestion] = useState("")
  const [selectedFile, setSelectedFile] = useState(null);
  const [airesponse, setAiresponse] = useState("");
  const Email = localStorage.getItem('userEmail');


  // fetch data from LLM
  async function generateAnswer() {
    setAiresponse("loading...")
    const response = await axios({
      method: 'post',
      url: 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyBi4RSjxcSs9yGe51E9pUnjK-C96hfuWiE',
      data: {
        "contents": [{
          "parts": [{ "text": question }]
        }]
      }
    })
    setAiresponse(response["data"]["candidates"][0]["content"]["parts"][0]["text"])
  }




  // Selecting and uploading the CSV file 
  // creating a FormData object, appending the file, and uploading it to the server
  const onFileUpload = () => {
    console.log("uploading")
    const formData = new FormData();
    formData.append(
      "myFile",
      selectedFile,
      selectedFile.name
    );
    console.log(selectedFile);
    // axios.post("api/uploadfile", formData);
  };

  // showing the file details and promting user to select the file
  const fileData = () => {
    if (selectedFile) {
      return (
        <div>
          <h2>File Details:</h2>
          <p>File Name: {selectedFile.name}</p>
          <p>File Type: {selectedFile.type}</p>
          <p>
            {/* Last Modified: {selectedFile.lastModifiedDate.toDateString()} */}
          </p>
        </div>
      );
    } else {
      const a = () => {
        return (
          <div>
            <br />
            <h4>Choose file before Pressing the Upload button</h4>
          </div>
        );
      }
    }
  };



  return (

    <>
      {/* chatbot logo */}
      <div>
        <a href="/home/cybertom/AI-app/AI-learner/src/assets/chatbot.png" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>

        <h3>ur lerning assistant</h3>

      </div>


      <div className='response'><p>{airesponse}</p></div>
      
      <h3>User : {Email}</h3> 


      <div className='allbuttons'>
        <div className='input1 input-group mb-3'>
          <textarea
            className='input'
            placeholder='Enter your lerning plan or upload the learning path file' value={question}
            onChange={(e) => setQuestion(e.target.value)}
            cols="8"
            rows="3"

          ></textarea>
        </div>

        <div className='downbuttons'>

          <input
            className='fileselect'
            //  field-sizing: content
            type="file"
            //  accept=".csv"
            onChange={(e) => {
              setSelectedFile(e.target.files[0]);
            }} />


          {/* CSV file uploading */}

          <button className="upbutton fileupload" onClick={onFileUpload}>
            Upload CSV file
          </button>
          {fileData()}

          <button className="sendbutton" onClick={generateAnswer}>
            send
          </button>

        </div>
      </div>
    </>


  )
}

export default App

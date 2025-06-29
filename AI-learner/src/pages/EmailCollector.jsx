import { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import '../App.css';
import axios from 'axios';

const EmailCollector = () => {
  const [email, setEmail] = useState('');
  const [userId, setUserId] = useState('');
  const [submitted, setSubmitted] = useState(false);
  const [response, setResponse] = useState('');  // ✅ Added to store backend response
  const navigate = useNavigate();

  // Load stored email and user ID on first render
  useEffect(() => {
    const storedEmail = localStorage.getItem('userEmail');
    const storedUserId = localStorage.getItem('userId');

    // ✅ Uncommented and properly closed the effect block
    if (storedEmail && storedUserId) {
      setEmail(storedEmail);
      setUserId(storedUserId);
      setSubmitted(true);
      sendEmailToBackend(storedEmail);  // Automatically send it
      navigate('./page1');
    }
  }, [navigate]);

  // Handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();

    // Use crypto.randomUUID() if available, fallback to Date.now()
    const newUserId =
      typeof crypto !== 'undefined' && crypto.randomUUID
        ? crypto.randomUUID()
        : Date.now().toString();

    localStorage.setItem('userEmail', email);
    localStorage.setItem('userId', newUserId);
    setUserId(newUserId);
    setSubmitted(true);
    sendEmailToBackend(email);  // ✅ Send to backend on submit too
    navigate('./page1');
  };

  // Reset stored data
  const handleReset = () => {
    localStorage.removeItem('userEmail');
    localStorage.removeItem('userId');
    setEmail('');
    setUserId('');
    setSubmitted(false);
  };

  /////// sending emaiil to the backend //////////
  const sendEmailToBackend = async (emailToSend) => {
    try {
      const res = await axios.post('http://localhost:5000/submit-email', {
        email: emailToSend
      });
      setResponse(res.data.message);  // ✅ Set backend response
    } catch (err) {
      console.error("Error sending email:", err);
      setResponse("Failed to send email.");
    }
  };

  // Show reset screen if user already submitted
  if (submitted) {
    return (
      <div>
        <p>Welcome, your email is: <strong>{email}</strong></p>
        <button onClick={handleReset}>Create New User ID</button>
        <p>{response}</p> {/* ✅ Show response if available */}
      </div>
    );
  }

  // Show email input form
  return (
    <div className='emailc'>
      <h2>Welcome! Let's get started</h2>
      <form onSubmit={handleSubmit}>
        <label htmlFor="email">Enter your email:</label><br />
        <input
          type="email"
          id="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        /><br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default EmailCollector;











// import { useState, useEffect } from 'react';
// import { useNavigate } from 'react-router-dom';
// import '../App.css' 
// import axios from 'axios';

// const EmailCollector = () => {
//   const [email, setEmail] = useState('');
//   const [userId, setUserId] = useState('');
//   const [submitted, setSubmitted] = useState(false);
//   const navigate = useNavigate();

//   // Load stored email and user ID on first render
//   useEffect(() => {
//     const storedEmail = localStorage.getItem('userEmail');
//     const storedUserId = localStorage.getItem('userId');

//   //   if (storedEmail && storedUserId) {
//   //     setEmail(storedEmail);
//   //     setUserId(storedUserId);
//   //     setSubmitted(true);
//   //     navigate('./page1');
//   //   }
//   // }, [navigate]);
// });

//   // Handle form submission
//   const handleSubmit = (e) => {
//     e.preventDefault();

//     // Use crypto.randomUUID() if available, fallback to Date.now()
//     const newUserId =
//       typeof crypto !== 'undefined' && crypto.randomUUID
//         ? crypto.randomUUID()
//         : Date.now().toString();

//     localStorage.setItem('userEmail', email);
//     localStorage.setItem('userId', newUserId);
//     setUserId(newUserId);
//     setSubmitted(true);
//     navigate('./page1');
//   };

//   // Reset stored data
//   const handleReset = () => {
//     localStorage.removeItem('userEmail');
//     localStorage.removeItem('userId');
//     setEmail('');
//     setUserId('');
//     setSubmitted(false);
//   };

//   // Show reset screen if user already submitted
//   if (submitted) {
//     return (
//       <div>
//         <p>Welcome, your email is: <strong>{email}</strong></p>
//         <button onClick={handleReset}>Create New User ID</button>
//       </div>
//     );
//   }

//   // Show email input form
//   return (
//     <div className='emailc'>
//       <h2>Welcome! Let's get started</h2>
//       <form onSubmit={handleSubmit}>
//         <label htmlFor="email">Enter your email:</label><br />
//         <input
//           type="email"
//           id="email"
//           value={email}
//           onChange={(e) => setEmail(e.target.value)}
//           required
//         /><br />
//         <button type="submit">Submit</button>
//       </form>
//     </div>
//   );
// };


// /////// sending emaiil to the backend //////////
// useEffect(() => {
//     // Get the stored email when the component loads
//     const storedEmail = localStorage.getItem('userEmail');
//     if (storedEmail) {
//       setEmail(storedEmail);
//       sendEmailToBackend(storedEmail);  // Automatically send it
//     }
//   }, []);

//   const sendEmailToBackend = async (emailToSend) => {
//     try {
//       const res = await axios.post('http://localhost:5000/submit-email', {
//         email: emailToSend
//       });
//       setResponse(res.data.message);
//     } catch (err) {
//       console.error("Error sending email:", err);
//       setResponse("Failed to send email.");
//     }
//   };

// export default EmailCollector;

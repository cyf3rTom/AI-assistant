import './App.css'
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import EmailCollector  from './pages/EmailCollector';
import Page1  from './pages/page1'
import Home from './pages/home'
import React from 'react';

const Main = () => {
  return (
      <Router>
        <Routes>
          {/* <Route path="/" element={<Home />} /> */}
          <Route path="/" element={<EmailCollector />} />
          <Route path="/page1" element={<Page1 />} />

        </Routes>
      </Router>
    
  );
}



export default Main;
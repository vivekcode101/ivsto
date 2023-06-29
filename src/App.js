import React, { useState } from 'react';

const App = () => {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleUploadData = async () => {
    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await fetch('/upload-data', {
        method: 'POST',
        body: formData
      });
      
      // Handle the response as needed
    } catch (error) {
      // Handle errors if any
    }
  };

  return (
    <div>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUploadData}>Upload Data</button>
    </div>
  );
};

export default App;

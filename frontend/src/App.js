// frontend/src/App.js
import React, { useState } from "react";

function App() {
  const [transaction, setTransaction] = useState({});
  const [prediction, setPrediction] = useState(null);

  const handleSubmit = async () => {
    const response = await fetch("http://localhost:5000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(transaction),
    });
    const data = await response.json();
    setPrediction(data.is_fraud);
  };

  return (
    <div>
      <h1>Fraud Detection</h1>
      {/* Form for entering transaction details */}
      {/* Display prediction */}
      {prediction !== null && <h2>Fraud: {prediction ? "Yes" : "No"}</h2>}
    </div>
  );
}

export default App;

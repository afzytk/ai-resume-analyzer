import { useState } from "react";

import Header from "./components/layout/Header";
import Footer from "./components/layout/Footer";
import Container from "./components/layout/Container";
import ResumeUpload from "./components/ResumeUpload";
import Result from "./components/Result";
import Loading from "./components/Loading";

import { analyzeResume } from "./services/api.js";

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (file) => {
    setLoading(true);
    setResult(null);

    try {
      const data = await analyzeResume(file);
      setResult(data);
    } catch (error) {
      alert("Failed to analyze resume");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center">
      <Header />

      <Container>
        <ResumeUpload onAnalyze={handleAnalyze} />
        {loading && <Loading />}
        <Result result={result} />
      </Container>

      <Footer />
    </div>
  );
}

export default App;
 
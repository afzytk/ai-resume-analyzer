import { useState } from "react";

function ResumeUpload({ onAnalyze = () => {} }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    const selectedFile = e.target.files?.[0] || null;
    setFile(selectedFile);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please select a resume file");
      return;
    }

    onAnalyze(file);
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-lg font-semibold text-gray-800 mb-2">
        Upload your resume
      </h2>

      <p className="text-sm text-gray-500 mb-4">
        Supported formats: PDF, DOC, DOCX
      </p>

      <form onSubmit={handleSubmit} className="space-y-4">
        <input
          type="file"
          accept=".pdf,.doc,.docx"
          onChange={handleFileChange}
          className="block w-full text-sm
            file:mr-4 file:py-2 file:px-4
            file:rounded-lg file:border-0
            file:bg-blue-50 file:text-blue-700
            hover:file:bg-blue-100"
        />

        <button
          type="submit"
          className="w-full bg-blue-600 text-white py-2 rounded-lg
                     hover:bg-blue-700 transition"
        >
          Analyze Resume
        </button>
      </form>
    </div>
  );
}

export default ResumeUpload;

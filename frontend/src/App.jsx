return (
  <div className="min-h-screen bg-gray-100 flex flex-col items-center">
    {/* Header */}
    <header className="w-full bg-white shadow-sm">
      <div className="max-w-4xl mx-auto px-6 py-4">
        <h1 className="text-2xl font-bold text-gray-800">
          AI Resume Analyzer
        </h1>
        <p className="text-gray-500 text-sm">
          Get ATS score and actionable feedback
        </p>
      </div>
    </header>

    {/* Main */}
    <main className="w-full max-w-4xl px-6 py-10">
      <ResumeUpload onAnalyze={handleAnalyze} />
      {loading && <p className="mt-4 text-blue-600">Analyzing resume...</p>}
      <Result result={result} />
    </main>
  </div>
);

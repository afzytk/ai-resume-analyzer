function Result({ result }) {
  if (!result) return null;

  return (
    <div className="bg-white rounded-xl shadow p-6 mt-6">
      <h2 className="text-xl font-semibold mb-4">
        Analysis Result
      </h2>

      <p className="mb-2">
        <strong>ATS Score:</strong> {result.ats_score}
      </p>

      <p className="mb-2">
        <strong>Job Fit Score:</strong> {result.job_fit_score}
      </p>

      <div className="mt-4">
        <h3 className="font-semibold">Feedback</h3>
        <ul className="list-disc pl-5">
          {result.feedback.map((item, idx) => (
            <li key={idx}>{item}</li>
          ))}
        </ul>
      </div>

      <div className="mt-4">
        <h3 className="font-semibold">Missing Skills</h3>
        <ul className="list-disc pl-5">
          {result.missing_skills.map((item, idx) => (
            <li key={idx}>{item}</li>
          ))}
        </ul>
      </div>

      <div className="mt-4">
        <h3 className="font-semibold">Missing Sections</h3>
        <ul className="list-disc pl-5">
          {result.missing_sections.map((item, idx) => (
            <li key={idx}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Result;

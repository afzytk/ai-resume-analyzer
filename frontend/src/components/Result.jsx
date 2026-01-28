import ATSScore from "./ATSScore";

function Result({ result }) {
  if (!result) return null;

  return (
    <div className="mt-8 space-y-6">
      <ATSScore score={result.ats_score} />

      <div className="bg-white rounded-xl shadow-md p-6">
        <h3 className="text-lg font-semibold mb-4">
          Resume Feedback
        </h3>

        <ul className="list-disc list-inside space-y-2 text-gray-700">
          {result.feedback.map((item, index) => (
            <li key={index}>{item}</li>
          ))}
        </ul>
      </div>
    </div>
  );
}

export default Result;

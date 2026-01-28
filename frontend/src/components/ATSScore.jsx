function ATSScore({ score }) {
  const getColor = () => {
    if (score >= 80) return "bg-green-500";
    if (score >= 50) return "bg-yellow-500";
    return "bg-red-500";
  };

  return (
    <div className="bg-white rounded-xl shadow-md p-6">
      <h2 className="text-gray-700 font-semibold mb-2">
        ATS Score
      </h2>

      <div className="w-full bg-gray-200 rounded-full h-4 overflow-hidden">
        <div
          className={`h-4 ${getColor()} transition-all duration-500`}
          style={{ width: `${score}%` }}
        />
      </div>

      <p className="text-center mt-4 text-2xl font-bold">
        {score}%
      </p>
    </div>
  );
}

export default ATSScore;

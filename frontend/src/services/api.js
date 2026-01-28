import axios from "axios";

const API_URL = "http://localhost:8000";

export const analyzeResume = async (
  file,
  jobRole = "",
  jobDescription = ""
) => {
  const formData = new FormData();
  formData.append("file", file);

  if (jobRole) {
    formData.append("job_role", jobRole);
  }

  if (jobDescription) {
    formData.append("job_description", jobDescription);
  }

  const response = await axios.post(
    `${API_URL}/upload-resume`,
    formData,
    {
      headers: {
        "Content-Type": "multipart/form-data",
      },
    }
  );

  return response.data;
};

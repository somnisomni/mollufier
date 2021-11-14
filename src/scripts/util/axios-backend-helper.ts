import axios from "axios";

export async function get(endpoint: string) {
  const response = await axios.get(`${process.env.VUE_APP_BACKEND_BASE_URL}/${endpoint}`, {
    responseType: "json",
  });

  return response.data;
}

export async function post(endpoint: string, jsonData: Record<string, unknown>) {
  const response = await axios.post(`${process.env.VUE_APP_BACKEND_BASE_URL}/${endpoint}`, jsonData, {
    responseType: "json",
  });

  return response.data;
}

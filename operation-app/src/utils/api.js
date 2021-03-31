import axios from "axios";
const BASE_URL = "http://127.0.0.1:8000";

const sleep = (milliseconds) => {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
};

export async function getData(params) {
  const response = await axios.get(BASE_URL + "/api/" + params.path);
  await sleep(500);
  return response.data;
}

export async function postData(params) {
  const response = await axios.post(
    BASE_URL + "/api/" + params.path + "/",
    params.data
  );
  await sleep(500);
  return response.data;
}

export async function putData(params) {
  const response = await axios.put(
    BASE_URL + "/api/" + params.path + "/",
    params.data
  );
  await sleep(900);
  response.data["processed"] = "COMPLETED";
  response.data["status"] = "COMPLETED";
  console.log("response", response.data);
  return response.data;
}

export async function deleteData(params) {
  const response = await axios.delete(BASE_URL + "/api/" + params.path);
  await sleep(500);
  return response.data;
}

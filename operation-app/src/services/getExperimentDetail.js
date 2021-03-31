import { getData } from "@/utils/api";
const PATH = "experiments";

export default function getExperimentDetail(id) {
  const response = getData({
    path: PATH + "/" + id,
  });
  console.log(response.data);
  return response;
}

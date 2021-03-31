import { postData } from "@/utils/api";
const PATH = "experiments";

export default function addExperiment(experiment) {
  const response = postData({
    path: PATH,
    data: experiment,
  });
  return response;
}

import { putData } from "@/utils/api";
const PATH = "experiments";

export default function runProcessing(experiment) {
  const experiment2 = experiment;
  experiment2.processed = "PENDING";
  const response = putData({
    path: PATH + "/runprocessing/" + experiment.id,
    data: experiment2,
  });
  return response;
}

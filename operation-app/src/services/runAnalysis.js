import { putData } from "@/utils/api";
const PATH = "analysis";

export default function runAnalysis(analysis) {
  const analysis2 = analysis;
  analysis2.status = "PENDING";
  const response = putData({
    path: PATH + "/runanalysis/" + analysis.id,
    data: analysis2,
  });
  return response;
}

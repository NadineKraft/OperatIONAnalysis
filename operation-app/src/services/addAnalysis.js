import { postData } from "@/utils/api";
const PATH = "analysis";

export default function addAnalysis(analysis) {
  const response = postData({
    path: PATH,
    data: analysis,
  });
  return response;
}

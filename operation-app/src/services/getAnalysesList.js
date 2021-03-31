import { getData } from "@/utils/api";
const PATH = "analysis";

export default function getAnalysisList() {
  const response = getData({
    path: PATH,
  });
  return response;
}

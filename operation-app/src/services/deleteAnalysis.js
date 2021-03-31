import { deleteData } from "@/utils/api";
const PATH = "analysis";

export default function deleteAnalysis(id) {
  const response = deleteData({
    path: PATH + "/" + id,
  });
  return response;
}

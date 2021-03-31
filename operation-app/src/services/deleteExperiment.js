import { deleteData } from "@/utils/api";
const PATH = "experiments";

export default function deleteExperiment(id) {
  const response = deleteData({
    path: PATH + "/" + id,
  });
  return response;
}

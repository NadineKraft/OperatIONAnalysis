import { deleteData } from "@/utils/api";
const PATH = "configs";

export default function deleteConfig(id) {
  const response = deleteData({
    path: PATH + "/" + id,
  });
  return response;
}

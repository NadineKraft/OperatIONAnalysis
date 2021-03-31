import { getData } from "@/utils/api";
const PATH = "configs";

export default function getConfigsList() {
  const response = getData({
    path: PATH,
  });
  return response;
}

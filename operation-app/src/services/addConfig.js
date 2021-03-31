import { postData } from "@/utils/api";
const PATH = "configs";

export default function addConfig(config) {
  const response = postData({
    path: PATH,
    data: config,
  });
  return response;
}

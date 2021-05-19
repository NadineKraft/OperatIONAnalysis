import { putConfig } from "@/utils/api";
const PATH = "configs";

export default function editConfig(config) {
  const response = putConfig({
    path: PATH + "/" + config.id,
    data: config,
  });
  return response;
}

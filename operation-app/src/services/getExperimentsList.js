import { getData } from "@/utils/api";
const PATH = "experiments";

export default function getExperimentsList() {
  const response = getData({
    path: PATH,
  });
  return response;
}

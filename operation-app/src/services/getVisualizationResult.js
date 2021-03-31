import { getData } from "@/utils/api";
const PATH = "visualization";

export default function getVisualizationResult() {
  const response = getData({
    path: PATH,
  });
  return response;
}

//export default async function getVisualizationResult() {
// const response = await fetch("./visualization/result_sequencing.html");
//  const text = await response.text();
//  document.getElementById("elementID").insertAdjacentText("beforeend", text);
//}

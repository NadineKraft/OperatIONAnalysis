import { putData } from "@/utils/api";

const PATH = "analysis";

export default function putStatus(analysis) {
  const analysis2 = analysis;
  analysis2.status = "COMPLETED";
  return putData({
    path: PATH + "/" + analysis.id,
    data: analysis2,
  });
}

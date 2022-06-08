import * as Backend from "./util/axios-backend-helper";

interface IMollufyRequest {
  sentence: string,
  options: {
    ignoreNounLengthLimit: boolean,
    changeMolluMark: boolean,
  },
}

interface IMollufyResponse {
  content: string,
}

export async function checkHealth(): Promise<boolean> {
  try {
    const content = await Backend.post("/mollufy", { sentence: "HEALTH CHECK" }) as IMollufyResponse;

    if(content.content) {
      return true;
    }
  } catch { /* NOOP */ }

  return false;
}

export default async function mollufy(request: IMollufyRequest): Promise<string | null> {
  try {
    const content = await Backend.post("/mollufy", request as unknown as Record<string, unknown>) as IMollufyResponse;

    return content.content;
  } catch {
    return null;
  }
}

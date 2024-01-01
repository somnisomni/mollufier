import * as Backend from "./util/backend-helper";

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
    const content = await Backend.post<IMollufyResponse>("/mollufy", { sentence: "HEALTH CHECK" });

    if(content && content.content) {
      return true;
    }
  } catch { /* NOOP */ }

  return false;
}

export default async function mollufy(request: IMollufyRequest): Promise<string | null> {
  try {
    const content = await Backend.post<IMollufyResponse>("/mollufy", request as unknown as Record<string, unknown>);

    return content?.content ?? null;
  } catch {
    return null;
  }
}

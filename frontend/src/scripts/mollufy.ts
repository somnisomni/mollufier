import * as Backend from "./util/axios-backend-helper";

interface IMollufyRequest {
  sentence: string,
  options: {
    ignoreNounLengthLimit: boolean,
  },
}

interface IMollufyResponse {
  content: string,
}

export default async function mollufy(request: IMollufyRequest): Promise<string> {
  const content = await Backend.post("/mollufy", request as unknown as Record<string, unknown>) as IMollufyResponse;

  return content.content;
}

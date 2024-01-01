const FETCH_COMMON_OPTIONS: RequestInit = {
  cache: "no-cache",
};

export async function get<T>(endpoint: string): Promise<T | null> {
  const response = await fetch(`${process.env.VUE_APP_BACKEND_BASE_URL}/${endpoint.replace(/^\/+/, "")}`, {
    ...FETCH_COMMON_OPTIONS,
  });

  if(!response.ok) return null;
  return await response.json() as T;
}

export async function post<T>(endpoint: string, jsonData: Record<string, unknown>): Promise<T | null> {
  const response = await fetch(`${process.env.VUE_APP_BACKEND_BASE_URL}/${endpoint.replace(/^\/+/, "")}`, {
    ...FETCH_COMMON_OPTIONS,
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(jsonData),
  });

  if(!response.ok) return null;
  return await response.json() as T;
}

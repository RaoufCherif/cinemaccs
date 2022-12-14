export type HttpVerb = "GET" | "POST" | "PUT" | "PATCH" | "DELETE";

export type RequestSearchParams = Record<
  string,
  string | string[] | null | undefined | boolean | number | number[]
>;
export interface RequestParams {
  urlValues?: Record<string, string | number>;
  searchParams?: RequestSearchParams;
}
export type APIQueryKey = [string, RequestParams?];

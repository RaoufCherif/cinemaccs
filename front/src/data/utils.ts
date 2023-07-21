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

export const sampleSessions = [
  {
    day: "Vendredi",
    date: "2021-10-10",
    time: "20:00",
    language: "VF",
    reservation_link: "https://codephenix.fr",
  },
  {
    day: "Vendredi",
    date: "2021-10-10",
    time: "22:00",
    language: "VO",
    reservation_link: "https://codephenix.fr",
  },
  {
    day: "Samedi",
    date: "2021-10-11",
    time: "22:00",
    language: "VO",
    reservation_link: "https://codephenix.fr",
  },
  {
    day: "Dimanche",
    date: "2021-10-12",
    time: "22:00",
    language: "VO",
    reservation_link: "https://codephenix.fr",
  },
];

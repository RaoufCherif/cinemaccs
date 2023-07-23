import {
  Box,
  Tabs,
  TabList,
  TabPanels,
  Tab,
  TabPanel,
  Spinner,
} from "@chakra-ui/react";
import { Day } from "./types";
import { useGetTheater } from "../data/theater";
import { PageLayout } from "../components/PageLayout";
import { TheaterCard, MovieRoomCard } from "../components/Cards";

export const TheaterPage = () => {
  //   TODO Make it work
  //   const days = theater.movies_rooms.map((mr) => mr.sessions.map((s) => s.day));
  //   const uniqueDays = days.filter((day) => onlyUnique(day, 0, days));
  const uniqueDays = ["Vendredi", "Samedi", "Dimanche"];
  const { data: theater, isLoading } = useGetTheater();
  return (
    <PageLayout isLoading={isLoading}>
      {theater ? (
        <>
          <TheaterCard theater={theater} />
          <Box>
            <Tabs>
              <TabList>
                {uniqueDays.map((day, idx) => (
                  <Tab key={`tab-${idx}`}>{day}</Tab>
                ))}
              </TabList>

              <TabPanels>
                {uniqueDays.map((day, idx) => (
                  <TabPanel key={`tabpanel-${idx}`}>
                    {theater.movies_rooms.map((mr, idx) => (
                      <MovieRoomCard
                        key={`movie-${idx}`}
                        movieRoom={mr}
                        day={day as Day}
                      />
                    ))}
                  </TabPanel>
                ))}
              </TabPanels>
            </Tabs>
          </Box>{" "}
        </>
      ) : (
        <Box>Cinéma introuvable</Box>
      )}
    </PageLayout>
  );
};

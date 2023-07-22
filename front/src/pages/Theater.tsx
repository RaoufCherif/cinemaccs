import * as React from "react";
import {
  Text,
  Flex,
  Box,
  Stack,
  Image,
  Tabs,
  TabList,
  TabPanels,
  Tab,
  TabPanel,
  Spinner,
} from "@chakra-ui/react";
import { Theater, MovieRoom, Day } from "./types";
import { useGetTheater } from "../data/theater";

const TheaterCard: React.FC<{ theater: Theater }> = ({ theater }) => {
  return (
    <Box>
      <Flex>
        <Image src={`data:image/jpeg;base64, ${theater.photos[0]}`} />
        <Flex ml={2} flexDir="column">
          <Box>{theater.name}</Box>
          <Box>{theater.address}</Box>
          <Box>{theater.accessibility_description}</Box>
        </Flex>
      </Flex>
      <Flex mt={2}>
        {theater.photos.map((photo, idx) => (
          <Image
            width="100px"
            mr={3}
            key={`photo-${idx}`}
            src={`data:image/jpeg;base64, ${photo}`}
          />
        ))}
      </Flex>
    </Box>
  );
};

const MovieCard: React.FC<{ movieRoom: MovieRoom; day: Day }> = ({
  movieRoom,
  day,
}) => {
  const { movie, room, sessions } = movieRoom;

  return (
    <Flex mb={2}>
      <Image
        mr={3}
        maxW="70px"
        src={`data:image/jpeg;base64, ${movie.poster}`}
      />
      <Box>
        <Text>
          {movie.title} - {room.name}
        </Text>
        <Flex>
          {sessions.map(
            (session, idx) =>
              session.day === day && (
                <Box key={`session-${idx}`} backgroundColor="yellow.300" mr={2}>
                  <Text>{session.language}</Text>
                  <Text>{session.time}</Text>
                </Box>
              ),
          )}
        </Flex>
      </Box>
    </Flex>
  );
};
export const TheaterPage = () => {
  //   TODO Make it work
  //   const days = theater.movies_rooms.map((mr) => mr.sessions.map((s) => s.day));
  //   const uniqueDays = days.filter((day) => onlyUnique(day, 0, days));
  const uniqueDays = ["Vendredi", "Samedi", "Dimanche"];
  const { data: theater, isLoading } = useGetTheater();
  if (isLoading) {
    return <Spinner />;
  }
  return (
    <Flex
      flexDirection="column"
      width="100wh"
      height="100vh"
      backgroundColor="gray.200"
      justifyContent="center"
      alignItems="center"
    >
      <Stack
        flexDir="column"
        mb="2"
        justifyContent="center"
        alignItems="center"
      >
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
                        <MovieCard
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
      </Stack>
    </Flex>
  );
};

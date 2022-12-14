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
} from "@chakra-ui/react";
import { sampleImage } from "../sample_image";
import { Theater, MovieRoom, Day } from "./types";

// function onlyUnique<T>(value: T, index: number, self: T[]): boolean {
//   return self.indexOf(value) === index;
// }

const movie_room = {
  movie: {
    id: "1",
    title: "Le chat poté",
    poster: sampleImage,
    duration: "3H12",
    allocine_link: "https://codephenix.fr",
  },
  room: {
    id: "1",
    name: "Salle 1",
  },
  sessions: [
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
  ],
};

const theater = {
  id: "1",
  name: "MK2 Bibliothèque",
  address: "2 rue de la bibliothèque, 75014 Paris",
  accessibility_description:
    "La salle est plutôt accessible mais les escaliers sont un peu raides. Si vous faites de l'escalade ca devrait aller mais sinon partez plutôt sur l'option home cinema",
  photos: [sampleImage, sampleImage, sampleImage],
  movies_rooms: [movie_room, movie_room, movie_room],
} as Theater;

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
              )
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
        </Box>
      </Stack>
    </Flex>
  );
};

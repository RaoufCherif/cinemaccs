import * as React from "react";
import {
  Card,
  CardBody,
  CardFooter,
  Button,
  Heading,
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
import { PageLayout } from "../components/PageLayout";

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
    <Card
      direction={{ base: "column", sm: "row" }}
      overflow="hidden"
      variant="outline"
    >
      <Image
        objectFit="cover"
        maxW={{ base: "100%", sm: "200px" }}
        src={`data:image/jpeg;base64, ${movie.poster}`}
        alt="Caffe Latte"
      />

      <Stack>
        <CardBody>
          <Heading size="md">
            {movie.title} - {room.name}
          </Heading>
          {sessions.map(
            (session, idx) =>
              session.day === day && (
                <Box key={`session-${idx}`} backgroundColor="yellow.300" mr={2}>
                  <Text>{session.language}</Text>
                  <Text>{session.time}</Text>
                </Box>
              ),
          )}
        </CardBody>

        <CardFooter>
          <Button variant="solid" colorScheme="blue">
            Buy Latte
          </Button>
        </CardFooter>
      </Stack>
    </Card>
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
    <PageLayout>
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
    </PageLayout>
  );
};

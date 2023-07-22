import { Flex, Box, Stack, Spinner, Image, Link } from "@chakra-ui/react";

import { useGetRoom } from "../data/room";
import { PageLayout } from "../components/PageLayout";

export const RoomPage = () => {
  const { isLoading, data: room } = useGetRoom();
  if (isLoading) {
    return <Spinner />;
  }
  return (
    <PageLayout>
      {room ? (
        <>
          {/* TODO utiliser TheaterCard ici */}
          <div>toto</div>
        </>
      ) : (
        <Box>Salle introuvable</Box>
      )}
    </PageLayout>
  );
};

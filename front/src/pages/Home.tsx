import * as React from "react";
import {
  Flex,
  Heading,
  Input,
  Button,
  InputGroup,
  Stack,
  InputLeftElement,
  Box,
  Link,
  Avatar,
  FormControl,
} from "@chakra-ui/react";
import { useGetTheaters } from "../data/theater";
import { PageLayout } from "../components/PageLayout";

export const HomePage = () => {
  const { data: theaters } = useGetTheaters();
  return (
    <PageLayout>
      <Avatar bg="teal.500" />
      <Heading color="teal.400">Bienvenue</Heading>
      <Box minW={{ base: "90%", md: "468px" }}>
        <form>
          <Stack
            spacing={4}
            p="1rem"
            backgroundColor="whiteAlpha.900"
            boxShadow="md"
          >
            <FormControl>
              <InputGroup>
                <InputLeftElement
                  pointerEvents="none"
                  //   children={<CFaUserAlt color="gray.300" />}
                />
                <Input type="text" placeholder="Le chat poté" />
              </InputGroup>
            </FormControl>
            <Button
              borderRadius={0}
              type="submit"
              variant="solid"
              colorScheme="teal"
              width="full"
            >
              Rechercher un film
            </Button>
          </Stack>
        </form>
      </Box>
      <Box minW={{ base: "90%", md: "468px" }}>
        <Stack
          spacing={4}
          p="1rem"
          backgroundColor="whiteAlpha.900"
          boxShadow="md"
        >
          {theaters ? (
            theaters.map((theater) => (
              <Link key={theater.id} href={`/cinema/${theater.id}`}>
                {theater.name}, {theater.address}
              </Link>
            ))
          ) : (
            <div>Aucun résultat</div>
          )}
        </Stack>
      </Box>
    </PageLayout>
  );
};

export default HomePage;

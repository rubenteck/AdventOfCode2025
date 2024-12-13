package cegeka.be.sah.adventofcode;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

import java.io.IOException;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
class AdventOfCodeApplicationTests {

    @Test
    void contextLoads() {
    }

    @Test
    void jsonFileReaderTest() throws IOException {
        FileReader fileReader = new FileReader();
        ToyList actualToyList = fileReader.readToyList();

        Toy expectedToy = new Toy("Train", "Toy", 5);
        ToyList expectedToyList = new ToyList(List.of(expectedToy));

        assertThat(actualToyList.toys()).containsExactlyInAnyOrderElementsOf(expectedToyList.toys());
    }

    @Test
    void calculateNumberOfToysByTypeTest() {

        String output = "{Clothing:3, Candy:30, Toys: 13}";

    }

    @Test
    void getMostPopularToyTest() {
        String output = "Candy";
    }



}

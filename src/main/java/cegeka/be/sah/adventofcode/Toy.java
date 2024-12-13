package cegeka.be.sah.adventofcode;

import com.fasterxml.jackson.annotation.JsonProperty;

public record Toy(
        @JsonProperty String name,
        @JsonProperty String type,
        @JsonProperty int amount
) {
}

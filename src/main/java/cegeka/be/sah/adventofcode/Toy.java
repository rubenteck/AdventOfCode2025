package cegeka.be.sah.adventofcode;

public record Toy(
        @JsonProperty String name,
        String type,
        int amount
) {
}

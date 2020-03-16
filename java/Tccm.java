import com.fasterxml.jackson.annotation.JsonInclude;
import com.fasterxml.jackson.annotation.JsonProperty;
import com.fasterxml.jackson.annotation.JsonPropertyDescription;
import com.fasterxml.jackson.annotation.JsonPropertyOrder;


/**
 * tccm
 * <p>
 * 
 * 
 */
@JsonInclude(JsonInclude.Include.NON_NULL)
@JsonPropertyOrder({
    "EntityReference",
    "NameAndMeaningReference",
    "OpaqueData"
})
public class Tccm {

    /**
     * EntityReference
     * <p>
     * 
     * 
     */
    @JsonProperty("EntityReference")
    @JsonPropertyDescription("")
    private EntityReference entityReference;
    /**
     * NameAndMeaningReference
     * <p>
     * 
     * 
     */
    @JsonProperty("NameAndMeaningReference")
    @JsonPropertyDescription("")
    private NameAndMeaningReference nameAndMeaningReference;
    /**
     * OpaqueData
     * <p>
     * 
     * 
     */
    @JsonProperty("OpaqueData")
    @JsonPropertyDescription("")
    private OpaqueData opaqueData;

    /**
     * EntityReference
     * <p>
     * 
     * 
     */
    @JsonProperty("EntityReference")
    public EntityReference getEntityReference() {
        return entityReference;
    }

    /**
     * EntityReference
     * <p>
     * 
     * 
     */
    @JsonProperty("EntityReference")
    public void setEntityReference(EntityReference entityReference) {
        this.entityReference = entityReference;
    }

    /**
     * NameAndMeaningReference
     * <p>
     * 
     * 
     */
    @JsonProperty("NameAndMeaningReference")
    public NameAndMeaningReference getNameAndMeaningReference() {
        return nameAndMeaningReference;
    }

    /**
     * NameAndMeaningReference
     * <p>
     * 
     * 
     */
    @JsonProperty("NameAndMeaningReference")
    public void setNameAndMeaningReference(NameAndMeaningReference nameAndMeaningReference) {
        this.nameAndMeaningReference = nameAndMeaningReference;
    }

    /**
     * OpaqueData
     * <p>
     * 
     * 
     */
    @JsonProperty("OpaqueData")
    public OpaqueData getOpaqueData() {
        return opaqueData;
    }

    /**
     * OpaqueData
     * <p>
     * 
     * 
     */
    @JsonProperty("OpaqueData")
    public void setOpaqueData(OpaqueData opaqueData) {
        this.opaqueData = opaqueData;
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append(Tccm.class.getName()).append('@').append(Integer.toHexString(System.identityHashCode(this))).append('[');
        sb.append("entityReference");
        sb.append('=');
        sb.append(((this.entityReference == null)?"<null>":this.entityReference));
        sb.append(',');
        sb.append("nameAndMeaningReference");
        sb.append('=');
        sb.append(((this.nameAndMeaningReference == null)?"<null>":this.nameAndMeaningReference));
        sb.append(',');
        sb.append("opaqueData");
        sb.append('=');
        sb.append(((this.opaqueData == null)?"<null>":this.opaqueData));
        sb.append(',');
        if (sb.charAt((sb.length()- 1)) == ',') {
            sb.setCharAt((sb.length()- 1), ']');
        } else {
            sb.append(']');
        }
        return sb.toString();
    }

    @Override
    public int hashCode() {
        int result = 1;
        result = ((result* 31)+((this.opaqueData == null)? 0 :this.opaqueData.hashCode()));
        result = ((result* 31)+((this.entityReference == null)? 0 :this.entityReference.hashCode()));
        result = ((result* 31)+((this.nameAndMeaningReference == null)? 0 :this.nameAndMeaningReference.hashCode()));
        return result;
    }

    @Override
    public boolean equals(Object other) {
        if (other == this) {
            return true;
        }
        if ((other instanceof Tccm) == false) {
            return false;
        }
        Tccm rhs = ((Tccm) other);
        return ((((this.opaqueData == rhs.opaqueData)||((this.opaqueData!= null)&&this.opaqueData.equals(rhs.opaqueData)))&&((this.entityReference == rhs.entityReference)||((this.entityReference!= null)&&this.entityReference.equals(rhs.entityReference))))&&((this.nameAndMeaningReference == rhs.nameAndMeaningReference)||((this.nameAndMeaningReference!= null)&&this.nameAndMeaningReference.equals(rhs.nameAndMeaningReference))));
    }

}

<template>
  <div>
    <div class="row m-0 justify-content-center mb-4">
      <h3 class="text-center my-3 y-line">식도랑 유저와 함께해요</h3>
    </div>
    <div class="mx-2" v-if="(partyList.length > 0)">
      <div v-for="(partyItem, index) in partyList" :key="index" class="item-wrap">
        <PartyListItem :partyItem="partyItem" :index="index" />
      </div>
    </div>
    <div v-else class="mx-2">
      <div>게시글이 없습니다.</div>
    </div>
  </div>
</template>

<script>
import PartyListItem from "@/components/party/PartyListItem.vue";
export default {
  name: "PartyList",
  components: {
    PartyListItem,
  },
  data() {
    return {
      partyList: [],
    };
  },
  mounted() {
    this.getPartyList();
  },
  methods: {
    getPartyList() {
      this.$axios
        .get(`/party/list_party`)
        .then((res) => {
          this.partyList = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>

<style scoped>
.y-line {
  border-top: 2px solid crimson;
  border-bottom: 2px solid crimson;
  padding: 0.5rem;
  font-weight: bolder;
}
.item-wrap {
  cursor: pointer;
}
</style>
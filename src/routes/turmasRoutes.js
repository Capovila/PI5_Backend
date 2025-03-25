import express from "express";
import * as turmasController from "../controllers/turmasController.js";

const router = express.Router();

router.get("/", turmasController.getTurmas);
router.get("/:id", turmasController.getTurmasById);

export default router;
